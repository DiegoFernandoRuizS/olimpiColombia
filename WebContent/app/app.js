require('./dependencies.js');
var appConfiguration;
var appModules = [
  'ngCookies',
  'ui.bootstrap',
  'pascalprecht.translate',
  'ngRoute',
  'i18nModule',
  'commonDirectivesModule',
  'mainModule',
  'firstComponentModule'
];

appConfiguration = appConfigurations.productionConfiguration;

angular.module('helloworldApp', appModules, appConfiguration);
angular.bootstrap(document, ['helloworldApp']);
