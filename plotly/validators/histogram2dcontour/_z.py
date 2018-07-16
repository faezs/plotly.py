import _plotly_utils.basevalidators


class ZValidator(_plotly_utils.basevalidators.DataArrayValidator):

    def __init__(
        self, plotly_name='z', parent_name='histogram2dcontour', **kwargs
    ):
        super(ZValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='data',
            **kwargs
        )
