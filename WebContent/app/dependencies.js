require('./../home.jade');
require('./vendors.js');

require('../app/appConfig.js');

/**
 * Global styles
 * styles of controls should be in each module
 **/
require('../app/styles/css/bootstrap.less');
require('../app/styles/css/bootstrap-theme.less');
require('../app/styles/css/app.less');

/**
 * Internationalization = i18n
 **/
require('../app/i18n/i18nModule.js');
require('../app/i18n/i18nDirective.js');
require('../app/i18n/i18nService.js');

/**
 * common Directives
 **/
require('../app/commons/directives/commonDirectivesModule.js');
require('../app/commons/directives/ripple/rippleDirective.js');
require('../app/commons/directives/ripple/ripple.less');

/**
 * common Services
 **/
require('../app/commons/services/commonServicesModule.js');
require('../app/commons/services/modal/modalService.js');


/**
 * mainComponent Module
 **/
require('../app/main/mainModule.js');
require('../app/main/mainComponent.js');
require('../app/main/main.less');


/**
 * sportList Module
 **/
 require('../app/sportList/sportListModule.js');
 require('../app/sportList/sportListComponent.js');
 require('../app/sportList/sportListService.js');
 require('../app/sportList/sportList.less');

require('../app/restApi/restApiModule.js');
require('../app/restApi/sportsApiService.js');

