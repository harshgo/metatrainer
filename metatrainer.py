class metatrainer:
    X = []
    y = []

    def gridsearch(self, model_name):
        pass # TODO

    def fit(self, X, y, lib_model_dict=None):
        if(lib_model_dict is not None):
            self.lib_model_dict=lib_model_dict
        else:
            self.lib_model_dict=default_lib_model_dict

        self.models = []
        self.X = X
        self.y = y
        for lib in lib_model_dict:
            self.models.append = [gridsearch(model) for model in lib_model_dict[lib]]
    return find_best(model)