import _plotly_utils.basevalidators


class TracerefminusValidator(_plotly_utils.basevalidators.IntegerValidator):

    def __init__(
        self,
        plotly_name='tracerefminus',
        parent_name='scattergl.error_x',
        **kwargs
    ):
        super(TracerefminusValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            min=0,
            role='info',
            **kwargs
        )
