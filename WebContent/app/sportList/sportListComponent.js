var  sportListModule = angular.module('sportListModule');
var SportListController = ['$i18n', 'SportListService', function ($i18n, SportListService) {
    /**
     * Tip: add here only visual logic
     */
    var self = this;
    self.sportList = SportListService;
    self.sportList.getSports();
    self.showAlert = function () {
        alert($i18n.translate.general_alert);
    };
}];

sportListModule.component('sportList', {
    transclude: true,
    bindings: {
        title: '@'
    },
    controller: SportListController,
    controllerAs: 'ctrl',
    template: require('./sportList.html')
});
