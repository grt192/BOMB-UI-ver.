from typing import Any


class Constants:

  def __setattr__(self, __name: str, __value: Any):
    raise AttributeError("Cannot modify Constants")

  def __new__(self, *args, **kwargs):
    raise AttributeError("Cannot create instance of Constants")
  
  MOTOR_TABLE_NAME = "Motors"