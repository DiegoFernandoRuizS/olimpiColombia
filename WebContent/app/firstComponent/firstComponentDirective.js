var firstComponentModule = angular.module('firstComponentModule');
firstComponentModule.controller('FirstComponentController', ['$i18n', function ($i18n) {
    /**
     * Tip: add here only visual logic
     */
    var vm = this;
    vm.showAlert = function () {
        alert($i18n.translate.general_alert);
    };
}]);

firstComponentModule.directive('firstComponent', [function () {
    return {
        restrict: 'E',
        scope: {},
        controller: 'FirstComponentController',
        controllerAs: 'ctrl',
        template: require('./firstComponent.html')
    };
}]);
