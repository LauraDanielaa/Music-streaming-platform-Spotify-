from abc import ABC, abstractmethod

class StateUser(ABC):
    """Base class for a user of the music service."""

    @abstractmethod
    def make_playlist(self):
        """Create a new playlist."""
        pass

    @abstractmethod
    def liste_music(self):
        """List all available music."""
        pass

class FreeUser(StateUser):
    """A user of the music service who has not subscribed."""
    def __init__(self):
        self.add = None

    def adds(self):
        """Display ads to the user."""
        self.add = Add(1, "Anuncio")
    
class Add():
    """An ad that is displayed to the user."""

    def __init__(self, id_ad, ad_content):
        """Initialize a new ad."""
        self.id_ad = id_ad
        self.ad_content = ad_content

    def display_ad(self):
        """Display the ad to the user."""
        pass


class SubscribedUser(StateUser):
    """A user of the music service who has a subscription."""

    def make_playlist(self):
        """Create a new playlist. Full functionality for subscribed users."""
        pass


    def ola(self):
        """Return a message indicating the user's subscription status."""
        return "pago"

class SubscriptionPayment:
    """A payment for a subscription to the music service."""

    def __init__(self, id_payment, id_user, album_name, payments_plan):
        """Initialize a new payment."""
        self.id_payment = id_payment
        self.id_user = id_user
        self.album_name = album_name
        self.payments_plan = payments_plan