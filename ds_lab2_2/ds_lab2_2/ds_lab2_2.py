from spyre import server
import vhi
#server.include_df_index = True


class StockExample(server.App):
    title = "VHI"

    inputs = [{
        "type": 'dropdown',
        "label": 'time_series',
        "options": [
            {"label": "VHI", "value": "VHI"},
            {"label": "VCI", "value": "VCI"},
            {"label": "TCI", "value": "TCI"}],
        "value": 'VHI',
        "key": 'time_series'
 
    },
        {"type": 'dropdown',
        "label": 'region',
        "options": [{"label": '%s'%(x), "value": '%s'%(x)} for x in range(1, 26)],
        "value": 'VHI',
        "key": 'region'},
        {"type":'dropdown',
        "label": 'start',
        "options" : [{"label": '%s'%(x), "value": '%s'%(x)} for x in range(1, 53)],
        "key": 'week_s'},
        {"type":'dropdown',
        "label": 'end',
        "options" : [{"label": '%s'%(x), "value": '%s'%(x)} for x in range(1, 53)],
        "key": 'week_e'}]

    controls = [{
        "type": "button",
        "id": "update_data",
        "label": "plot"
    }]

    tabs = ["Table","Plot"]

    outputs = [
        {
            "type": "plot",
            "id": "plot",
            "control_id": "update_data",
            "tab": "Plot"},
        {
            "type": "table",
            "id": "table_id",
            "control_id": "update_data",
            "tab": "Table"
        }
    ]

    def getData(self, params):
        region=params['region']
        time_series=params['time_series']
        start=params['week_s']
        end=params['week_e']
        df=vhi.general(region)
        df=df[(df['week']<=float(end)) & (df['week']>=float(start))]
        return df[[time_series]]
      

    def getPlot(self, params):
        df = self.getData(params)
        plt_obj = df.plot()
        plt_obj.set_ylabel("Data")
        plt_obj.set_xlabel("")
        plt_obj.set_title(params['region'])
        return plt_obj.get_figure()



app = StockExample()
app.launch()