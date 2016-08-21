"""Dose GUI for TDD: about dialog box."""
import wx
from . import __version__, __url__
from .rest import single_line_block
from .misc import snake2ucamel
from .shared import README, CONTRIBUTORS, LICENSE


metadata = {
  "copyright": single_line_block("copyright", README),
  "developers": CONTRIBUTORS,
  "description": single_line_block("summary", README),
  "version": __version__,
  "name": "Dose",
  "license": LICENSE,
  "web_site": __url__,
}


def about_box():
    """A simple about box dialog using the distribution data files."""
    about_info = wx.AboutDialogInfo()
    for k, v in metadata.items():
        setattr(about_info, snake2ucamel(k), v)
    wx.AboutBox(about_info)
