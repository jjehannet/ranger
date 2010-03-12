#!/usr/bin/python
# coding=utf-8
#
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

if __name__ == '__main__':
	import sys, pickle

	protocol = 0
	table = {}

	for line in open(len(sys.argv) > 1 and sys.argv[1] or "mime.types"):
		if len(line) > 3 and line[0] != '#' and ('\t' in line or ' ' in line):
			arr = line.split()
			name = arr[0]
			extensions = arr[1:]
			for ext in extensions:
				table[ext] = name

	pickle.dump(table, open('mime.dat', 'wb'), protocol)