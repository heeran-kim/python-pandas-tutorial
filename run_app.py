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

        file_path = './part_wine_reviews.csv'
        self.df = pd.read_csv(file_path)
        self.table = DataTable(self.df)
        self.m_grid1.SetTable(self.table, takeOwnership=True)
        self.m_grid1.AutoSize()

        self.Show(True)
        self.Layout()
        
    # Overload your event function
    def OnSearch( self, event ):
        event.Skip()
        
        min_value = float(self.m_textCtrl1.GetValue())
        max_value = float(self.m_textCtrl2.GetValue())

        df_filtered = self.df[self.df["price"] <= max_value]
        df_filtered = df_filtered[df_filtered["price"] >= min_value]

        # ser_prices = self.df["price"]
        # index = []
        # for price in ser_prices:
        #     if min_value <= price <= max_value:
        #         index.append(True)
        #     else:
        #         index.append(False)
        # df_filtered = self.df[index]
        
        self.m_grid1.ClearGrid()
        self.table = DataTable(df_filtered)
        self.m_grid1.SetTable(self.table, takeOwnership=True)
        self.m_grid1.AutoSize()
        
        text = f"The number of rows: {len(df_filtered)}"
        self.m_staticText4.SetLabel(text)


if __name__ == "__main__":
    app = wx.App()
    frame = CalcFrame()
    app.MainLoop()