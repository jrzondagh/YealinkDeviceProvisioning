from Crypto import Random 
from Crypto.Cipher import AES 

class YealinkCrypto:
	def __init__(self, block_size, key_length):
		self.block_size = block_size
		self.key_length = key_length
	
	def encrypt(self, raw, key):
		if len(key) <= self.key_length:
			key = key[:self.key_length]
		else:             
			key = self._pad(key)
			raw = self._pad(raw)
			iv = '\0' * self.key_length
			cipher = AES.new(key, AES.MODE_ECB, iv)
			enc = cipher.encrypt(raw)
		
		return enc

	def decrypt(self, enc, key):
		if len(key) <= self.key_length:
			key = key[:self.key_length]
		else:
			key = self._pad(key)
			iv = '\0' * self.key_length
			cipher = AES.new(key, AES.MODE_ECB, iv)
			raw = self._unpad(cipher.decrypt(enc))
		
		return raw

	def _pad(self, s):
		return s + (self.block_size - len(s) % self.block_size) * chr(self.block_size - len(s) % self.block_size)

	def _unpad(self, s):
		return s[:-ord(s[len(s)-1:])]
