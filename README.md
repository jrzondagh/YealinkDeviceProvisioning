# YealinkDeviceProvisioning
A library for encrypting Yealink Device Provisioning data

## Example usage

# python Python 2.7.3 (default, Feb 27 2014, 19:58:35) [GCC 4.6.3] on linux2 Type "help", "copyright", "credits" or "license" for more information.
>>> from yealink_crypto import YealinkCrypto
>>> c = YealinkCrypto(128, 16)
>>> enc = c.encrypt('123123123', '1234567890abcdef')
>>> dec = c.decrypt(enc, '1234567890abcdef')
>>> dec '123123123'
