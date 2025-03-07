#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
Example to show selecting a message into Subscriptions on a Topic using various Filters.
"""

import os
import time
from azure.core.exceptions import ResourceNotFoundError, ResourceExistsError
from azure.servicebus.management import (
    ServiceBusAdministrationClient,
    TrueRuleFilter,
    SqlRuleFilter,
    SqlRuleAction,
    CorrelationRuleFilter,
)
from azure.servicebus import ServiceBusMessage, ServiceBusClient
from azure.identity import DefaultAzureCredential

FULLY_QUALIFIED_NAMESPACE = os.environ["SERVICEBUS_FULLY_QUALIFIED_NAMESPACE"]
TOPIC_NAME = os.environ["SERVICEBUS_TOPIC_NAME"]
ALL_MSGS_SUBSCRIPTION_NAME = "sb-allmsgs-sub"
SQL_FILTER_ONLY_SUBSCRIPTION_NAME = "sb-sqlfilteronly-sub"
SQL_FILTER_WITH_ACTION_SUBSCRIPTION_NAME = "sb-sqlfilteraction-sub"
CORRELATION_FILTER_SUBSCRIPTION_NAME = "sb-corrfiltersub"


def create_rules_with_filter(servicebus_mgmt_client):
    # First subscription is already created with default rule. Leave as is.
    print("SubscriptionName: {}, Removing and re-adding Default Rule".format(ALL_MSGS_SUBSCRIPTION_NAME))
    create_rule_with_filter(servicebus_mgmt_client, ALL_MSGS_SUBSCRIPTION_NAME, "$Default", filter=TrueRuleFilter())

    # Second subscription: Add required SqlRuleFilter Rule.
    print(
        "SubscriptionName: {}, Removing Default Rule and Adding SqlRuleFilter.".format(
            SQL_FILTER_ONLY_SUBSCRIPTION_NAME
        )
    )
    create_rule_with_filter(
        servicebus_mgmt_client, SQL_FILTER_ONLY_SUBSCRIPTION_NAME, "RedSqlRule", filter=SqlRuleFilter("Color = 'Red'")
    )

    # Third subscription: Add SqlRuleFilter and SqlRuleAction.
    print(
        "SubscriptionName: {}, Removing Default Rule and Adding SqlRuleFilter and SqlRuleAction".format(
            SQL_FILTER_WITH_ACTION_SUBSCRIPTION_NAME
        )
    )
    create_rule_with_filter(
        servicebus_mgmt_client,
        SQL_FILTER_WITH_ACTION_SUBSCRIPTION_NAME,
        "BlueSqlRule",
        filter=SqlRuleFilter("Color = 'Blue'"),
        action=SqlRuleAction("SET Color = 'BlueProcessed'"),
    )

    # Fourth subscription: Add CorrelationRuleFilter.
    print(
        "SubscriptionName: {}, Removing Default Rule and Adding CorrelationRuleFilter".format(
            CORRELATION_FILTER_SUBSCRIPTION_NAME
        )
    )
    create_rule_with_filter(
        servicebus_mgmt_client,
        CORRELATION_FILTER_SUBSCRIPTION_NAME,
        "ImportantCorrelationRule",
        filter=CorrelationRuleFilter(correlation_id="important", label="Red"),
    )

    # Get rules on subscription, called here only for one subscription as an example.
    print("SubscriptionName: {}".format(CORRELATION_FILTER_SUBSCRIPTION_NAME))
    for rule in servicebus_mgmt_client.list_rules(TOPIC_NAME, CORRELATION_FILTER_SUBSCRIPTION_NAME):
        print("Rule {}; Filter: {}".format(rule.name, type(rule.filter).__name__))


def create_rule_with_filter(servicebus_mgmt_client, subscription_name, filter_name, filter, action=None):
    try:
        servicebus_mgmt_client.delete_rule(TOPIC_NAME, subscription_name, "$Default")
    except ResourceNotFoundError:
        pass
    try:
        servicebus_mgmt_client.create_rule(TOPIC_NAME, subscription_name, filter_name, filter=filter, action=action)
    except ResourceExistsError:
        pass


def send_messages():
    credential = DefaultAzureCredential()
    servicebus_client = ServiceBusClient(FULLY_QUALIFIED_NAMESPACE, credential)
    print("====================== Sending messages to topic ======================")
    msgs_to_send = []
    with servicebus_client.get_topic_sender(topic_name=TOPIC_NAME) as sender:
        msgs_to_send.append(create_message(label="Red"))
        msgs_to_send.append(create_message(label="Blue"))
        msgs_to_send.append(create_message(label="Red", correlation_id="important"))
        msgs_to_send.append(create_message(label="Blue", correlation_id="important"))
        msgs_to_send.append(create_message(label="Red", correlation_id="notimportant"))
        msgs_to_send.append(create_message(label="Blue", correlation_id="notimportant"))
        msgs_to_send.append(create_message(label="Green"))
        msgs_to_send.append(create_message(label="Green", correlation_id="important"))
        msgs_to_send.append(create_message(label="Green", correlation_id="notimportant"))
        sender.send_messages(msgs_to_send)


def create_message(label, correlation_id=None):
    return ServiceBusMessage(
        "Rule with filter sample", application_properties={"Color": label}, subject=label, correlation_id=correlation_id
    )


def receive_messages(servicebus_client, subscription_name):
    with servicebus_client:
        receiver = servicebus_client.get_subscription_receiver(
            topic_name=TOPIC_NAME, subscription_name=subscription_name
        )
        with receiver:
            print("==========================================================================")
            print("Receiving Messages From Subscription: {}".format(subscription_name))
            received_msgs = receiver.receive_messages(max_message_count=10, max_wait_time=5)
            for msg in received_msgs:
                color = msg.application_properties.get(b"Color").decode()
                correlation_id = msg.correlation_id
                print("Color Property = {}, Correlation ID = {}".format(color, correlation_id))
                receiver.complete_message(msg)
            print("'{}' Messages From Subscription: {}".format(len(received_msgs), subscription_name))
            print("==========================================================================")


def create_subscription(servicebus_mgmt_client, subscription_name):
    try:
        servicebus_mgmt_client.create_subscription(TOPIC_NAME, subscription_name)
    except ResourceExistsError:
        pass
    print("Subscription {} is created.".format(subscription_name))


def delete_subscription(servicebus_mgmt_client, subscription_name):
    try:
        servicebus_mgmt_client.delete_subscription(TOPIC_NAME, subscription_name)
    except ResourceNotFoundError:
        pass
    print("Subscription {} is deleted.".format(subscription_name))


if __name__ == "__main__":
    credential = DefaultAzureCredential()
    servicebus_mgmt_client = ServiceBusAdministrationClient(FULLY_QUALIFIED_NAMESPACE, credential)
    servicebus_client = ServiceBusClient(FULLY_QUALIFIED_NAMESPACE, credential)

    # Create subscriptions.
    create_subscription(servicebus_mgmt_client, ALL_MSGS_SUBSCRIPTION_NAME)
    create_subscription(servicebus_mgmt_client, SQL_FILTER_ONLY_SUBSCRIPTION_NAME)
    create_subscription(servicebus_mgmt_client, SQL_FILTER_WITH_ACTION_SUBSCRIPTION_NAME)
    create_subscription(servicebus_mgmt_client, CORRELATION_FILTER_SUBSCRIPTION_NAME)

    # Create rules
    create_rules_with_filter(servicebus_mgmt_client)

    # Send messages to topic
    send_messages()

    # Receive messages from 'ALL_MSGS_SUBSCRIPTION_NAME'. Should receive all 9 messages.
    receive_messages(servicebus_client, ALL_MSGS_SUBSCRIPTION_NAME)

    # Receive messages from 'SQL_FILTER_ONLY_SUBSCRIPTION_NAME'. Should receive all messages with Color = 'Red' i.e 3 messages
    receive_messages(servicebus_client, SQL_FILTER_ONLY_SUBSCRIPTION_NAME)

    # Receive messages from 'SQL_FILTER_WITH_ACTION_SUBSCRIPTION_NAME'. Should receive all messages with Color = 'Blue'
    # i.e 3 messages AND all messages should have color set to 'BlueProcessed'
    receive_messages(servicebus_client, SQL_FILTER_WITH_ACTION_SUBSCRIPTION_NAME)

    # Receive messages from 'CORRELATION_FILTER_SUBSCRIPTION_NAME'. Should receive all messages  with Color = 'Red' and CorrelationId = "important"
    # i.e 1 message
    receive_messages(servicebus_client, CORRELATION_FILTER_SUBSCRIPTION_NAME)

    # Delete subscriptions.
    delete_subscription(servicebus_mgmt_client, ALL_MSGS_SUBSCRIPTION_NAME)
    delete_subscription(servicebus_mgmt_client, SQL_FILTER_ONLY_SUBSCRIPTION_NAME)
    delete_subscription(servicebus_mgmt_client, SQL_FILTER_WITH_ACTION_SUBSCRIPTION_NAME)
    delete_subscription(servicebus_mgmt_client, CORRELATION_FILTER_SUBSCRIPTION_NAME)
