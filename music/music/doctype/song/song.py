# Copyright (c) 2024, Frappe Technologies Pvt Ltd and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import slug


class Song(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		artist: DF.Data | None
		cover_image: DF.AttachImage | None
		duration: DF.Data | None
		is_liked: DF.Check
		music_file: DF.Attach | None
		route: DF.Data | None
		title: DF.Data | None
	# end: auto-generated types

	def autoname(self):
		if not self.name:
			self.name = f"{slug(self.title)}"

	@frappe.whitelist()
	def like_song(self) -> None:
		self.is_liked = True
		self.save()

	def validate(self):
		self.route = f"/beats/song/{slug(self.title)}"
