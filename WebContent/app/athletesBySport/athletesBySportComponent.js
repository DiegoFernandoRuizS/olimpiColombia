var athletesBySportModule = angular.module('athletesBySportModule');
var AthletesBySportController = ['SportListService', '$bzModal', function (SportListService, $bzModal) {
    var self = this;
    self.sportListService = SportListService;
    self.closeModalAthletesBySport = function () {
        $bzModal.closePopup();
    };
}];

athletesBySportModule.component('athletesBySport', {
    transclude: true,
    bindings: {
        title: '@'
    },
    controller: AthletesBySportController,
    controllerAs: 'ctrl',
    template: require('./athletesBySport.html')
});
