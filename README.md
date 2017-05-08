# loxberry-smsgateway
This loxberry plugin redirects incoming SMS messages to Loxone Mini Server and can send SMS to phones according to requests from Loxone Mini Server

## Sending SMS

```
/send_sms?number=<phone-number>&message=<some-message>
```

The phone number should be given with country prefix, without leading zeros
or leading plus sign. Other formats might work, but this is the safest.

Example:

```
/send_sms?number=43123412345678&message=Hello%20World!
```

## Performing a voice call

```
/voice_call?number=<phone-number>&duration=<number-in-seconds>
```

Performs a voice call to the given number and waits for the given duration
in seconds until hanging up. The duration must be high enough to account for
waiting times until the connection to the target phone is established. This
usually can take a few seconds, so your duration should be long enough (e.g.
15 seconds).

Example:

```
/voice_call?number=43123412345678&duration=15
```
