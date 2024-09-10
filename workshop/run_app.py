import wx
import wx.grid
import pandas as pd
import re

from template_frame import MyFrame2 as MyFrame1

EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'


class DataTable(wx.grid.GridTableBase):
    def __init__(self, data=None):
        wx.grid.GridTableBase.__init__(self)
        self.headerRows = 1
        self.data = data

    def GetNumberRows(self):
        return len(self.data.index)

    def GetNumberCols(self):
        return len(self.data.columns)

    def GetValue(self, row, col):
        return self.data.iloc[row, col]

    def SetValue(self, row, col, value):
        self.data.iloc[row, col] = value

    # For better visualisation
    def GetColLabelValue(self, col):
        return self.data.columns[col]

    def GetAttr(self, row, col, prop):
        attr = wx.grid.GridCellAttr()
        if row % 2 == 1:
            attr.SetBackgroundColour(EVEN_ROW_COLOUR)
        return attr



class CalcFrame(MyFrame1):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.Show(True)
        self.Layout()
        
    # Overload your event function
    


if __name__ == "__main__":
    app = wx.App()
    frame = CalcFrame()
    app.MainLoop()