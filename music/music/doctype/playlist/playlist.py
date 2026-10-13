# Copyright (c) 2024, Frappe Technologies Pvt Ltd and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Playlist(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		from music.music.doctype.playlist_song.playlist_song import PlaylistSong

		songs: DF.Table[PlaylistSong]
		title: DF.Data | None
	# end: auto-generated types

	pass
