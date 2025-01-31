class URLBuilder:
    @staticmethod
    def format(endpoint, **kwargs):
        """Replace placeholders dynamically in endpoints"""
        return endpoint.format(**kwargs)