var sportListModule = angular.module('sportListModule');
var SportListController = ['$i18n', 'SportListService', '$bzModal', function ($i18n, SportListService, $bzModal) {
    /**
     * Tip: add here only visual logic
     */
    var self = this;
    self.sportListService = SportListService;
    self.sportListService.getSports();
    self.showAlert = function () {
        alert($i18n.translate.general_alert);
    };
    self.showModalAthletesBySport = function (sport) {
        console.log(sport.name);
        self.sportListService.getAthletesBySport(sport);
        $bzModal.showPopup({}, {
            template: '<athletes-by-sport title ="AthletesBySport"> </athletes-by-sport>',
            size: '600px'
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
