

from typing import List, Optional


class AvoidDisinformation:
	SLOGAN: str = "AVOID DISINFORMATION"

	def __init__(self) -> None:
		"""
        The name accountList is misleading because it suggests that the list contains Account objects,
        and list is also misleading because the variable is actually an array. 
        List is a more appropriate name for a collection that implements the List interface.
        """
		# actually contains User ids
		self.account_list: Optional[List[int]] = None

		# home phone number
		self.hp: Optional[str] = None

		# win times
		self.win: int = 0

		# date of birth
		self.db: Optional[str] = None

		# user registration list
		self.url: Optional[List] = None

	def exampleO01l(self, l: int, O: int, O1: int) -> int:
		"""
		Avoid using O,0,l,1.

		This method demonstrates confusing names and control flow.
		"""
		a = l
		if O == l:
			a = O1
		else:
			# Java used literal 01 (octal). Use 1 here for the same effect.
			l = 1

		return a if a > l else l

