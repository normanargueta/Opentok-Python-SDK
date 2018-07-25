from six import text_type, u
from .exceptions import OpenTokException

class Session(object):
    """
    Represents an OpenTok session.

    Use the OpenTok.create_session() method to create an OpenTok session. Use the
    session_id property of the Session object to get the session ID.

    :ivar String session_id: The session ID.
    """
    def __init__(self, sdk, session_id, **kwargs):
        if not text_type(session_id):
            raise OpenTokException(u('Cannot instantiate Session, session_id was not valid {0}').format(session_id))
        self.session_id = session_id
        self.sdk = sdk
        for key, value in kwargs.items():
            setattr(self, key, value)

    def generate_token(self, **kwargs):
        """
          Generates a token for the session.

          :param String role: The role for the token. Valid values are defined in the Role
            class.

            * `Roles.subscriber` -- A subscriber can only subscribe to streams.

            * `Roles.publisher` -- A publisher can publish streams, subscribe to
              streams, and signal. (This is the default value if you do not specify a role.)

            * `Roles.moderator` -- In addition to the privileges granted to a
              publisher, in clients using the OpenTok.js 2.2 library, a moderator can call the
              `forceUnpublish()` and `forceDisconnect()` method of the
              Session object.

          :param int expire_time: The expiration time of the token, in seconds since the UNIX epoch.
            The maximum expiration time is 30 days after the creation time. The default expiration
            time is 24 hours after the token creation time.

          :param String data: A string containing connection metadata describing the
            end-user. For example, you can pass the user ID, name, or other data describing the
            end-user. The length of the string is limited to 1000 characters. This data cannot be
            updated once it is set.

          :rtype:
            The token string.
        """
        return self.sdk.generate_token(self.session_id, **kwargs)

    def signal(self, *kwargs):
      """
      Send signals to all participants in an active OpenTok session or to a specific client
      connected to that session.
      
      :param String session_id: The session ID of the OpenTok session that receives the signal

      :param Dictionary: Structure that contains both the type and data fields. These correspond
      to the type and data parameters passed in the client signal received handlers

      :param connection_id String Optional: If it's present the signal is just send to that
      connection_id
      """
      return self.sdk.signal(self.session_id, *kwargs)

    def get_stream(self, *kwargs):
      """
      Returns an Stream object that contains information of an OpenTok stream:
      
      -id: The stream ID
      -videoType: "camera" or "screen"
      -name: The stream name (if one was set when the client published the stream)
      -layoutClassList: It's an array of the layout classes for the stream
      """
      return self.sdk.get_stream(self.session_id, *kwargs)
