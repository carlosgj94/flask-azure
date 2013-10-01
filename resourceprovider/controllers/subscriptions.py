"""
TODO: what are the subscription controllers?
"""


def registered(subscription_id, body):
    """
    This tells the RP that the user intends to create a resource under this subscription.
    """
    raise NotImplementedError


def disabled(subscription_id, body):
    """
    The user's Windows Azure subscription has been disabled, due to fraud or non-payment.
    Your RP should make the resource inaccessible without deleting its data.
    """
    raise NotImplementedError


def enabled(subscription_id, body):
    """
    The user's Windows Azure subscription has been enabled, because it is current on payments.
    Your RP should restore access to data.
    """
    raise NotImplementedError


def deleted(subscription_id, body):
    """
    The user's Windows Azure subscription has been deleted.
    Disable access permanently, but ensure the data is retained for at least 90 days.
    """
    raise NotImplementedError
