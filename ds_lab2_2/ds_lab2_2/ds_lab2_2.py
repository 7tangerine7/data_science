from spyre import server
from vhi import general, analyze, month
server.include_df_index = True


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
        "options": [{"label":str(x), "value": str(x)} for x in range(1, 26)],
        "value": 'VHI',
        "key": 'region'},
        {"type":'dropdown',
        "label": 'start',
        "options" : [{"label": str(x), "value": str(x)} for x in range(1, 53)],
        "key": 'week_s'},
        {"type":'dropdown',
        "label": 'end',
        "options" : [{"label": str(x), "value": str(x)} for x in range(1, 53)],
        "key": 'week_e'}]

    controls = [{
        "type": "button",
        "id": "update_data",
        "label": "plot"
    }]

    tabs = ["Table","Plot","Table2","Plot2"]

    outputs = [
        {
            "type": "plot",
            "id": "plot_id",
            "control_id": "update_data",
            "tab": "Plot"},
            {
            "type": "plot",
            "id": "plot_id2",
            "control_id": "update_data",
            "tab": "Plot2"},
        {
            "type": "table",
            "id": "table_id",
            "control_id": "update_data",
            "tab": "Table"
        },
         {
            "type": "table",
            "id": "table_id2",
            "control_id": "update_data",
            "tab": "Table2"
        }

    ]

    def table_id(self, params):
        region=params['region']
        time_series=params['time_series']
        start=params['week_s']
        end=params['week_e']
        df=general(region)
        df=df[(df['week']<=float(end)) & (df['week']>=float(start))]
        return df[[time_series]]
      
    def table_id2(self, params):
        region=params['region']
        time_series=params['time_series']
        start=params['week_s']
        end=params['week_e']
        df=general(region)
        return  month(df)

    def plot_id(self, params):
        df = self.table_id(params)
        plt_obj = df.plot()
        plt_obj.set_ylabel("Data")
        plt_obj.set_xlabel("")
        plt_obj.set_title(params['region'])
        return plt_obj.get_figure()

    def plot_id2(self, params):
        df = self.table_id2(params)
        plt_obj = df.plot()
        plt_obj.set_ylabel("Data")
        plt_obj.set_xlabel("")
        plt_obj.set_title(params['region'])
        return plt_obj.get_figure()



app = StockExample()
app.launch()