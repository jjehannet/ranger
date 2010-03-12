# Copyright (C) 2009, 2010  Roman Zimbelmann <romanz@lavabit.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class LazyParser(object):
	"""Parse commands and extract information"""
	def __init__(self, line):
		self.line = line
		self._chunks = None
		self._rests = None
		self._rests_loaded = 0
		self._rests_gen_instance = None

		try:
			self.firstpart = line[:line.rindex(' ') + 1]
		except ValueError:
			self.firstpart = ''

	def chunk(self, n, otherwise=''):
		"""Chunks are pieces of the command seperated by spaces"""
		if self._chunks is None:
			self._chunks = self.line.split()

		if len(self._chunks) > n:
			return self._chunks[n]
		else:
			return otherwise

	def rest(self, n, otherwise=''):
		"""Rests are the strings which come after each word."""
		if self._rests is None:
			self._rests = list(self._rest_generator())
			# TODO: Don't calculate all the rest elements if not needed

		if len(self._rests) > n:
			return self._rests[n]
		else:
			return otherwise

	def _rest_generator(self):
		lastrest = self.line
		n = 0
		while n < len(lastrest):
			if lastrest[n] == ' ':
				n += 1
			else:
				yield lastrest[n:]
				n = lastrest.find(' ', n) + 1
				if n <= 0:
					break
				lastrest = lastrest[n:]
				n = 0

	def __add__(self, newpart):
		return self.firstpart + newpart