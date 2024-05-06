from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def Classify_click(self, **event_args):
   
    """This method is called when the button is clicked"""
    # Call the google colab function and pass it the iris measurements
    sarcasm = anvil.server.call('predict_sarcasm', 
                                self.headline.text,)
    # If a category is returned set our species 
    if sarcasm:
      self.Classification.text = "the text is " + sarcasm.capitalize()