var sportListModule = angular.module('sportListModule');
var SportListController = ['$i18n', 'SportListService', '$bzModal', function ($i18n, SportListService, $bzModal) {
    /**
     * Tip: add here only visual logic
     */
    var self = this;
    self.sportList = SportListService;
    self.sportList.getSports();
    self.showAlert = function () {
        alert($i18n.translate.general_alert);
    };
    self.showModalAthletesBySport = function (sport) {
        console.log(sport.name);
        self.sportList.sportSelected = sport;
        $bzModal.showPopup({}, {
            template: '<span>Boxeo</span>',
            size: '300px'
        });
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
