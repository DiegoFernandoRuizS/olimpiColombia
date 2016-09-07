describe('Module to test: athletesBySport', function () {
   var element;
    beforeEach(module('athletesBySportModule'));
    beforeEach(module('pascalprecht.translate'));
    /***
     * Test for directive
     * */
    describe('athletesBySport directive', function () {
        var $compile,
            $rootScope;
        beforeEach(inject(function (_$compile_, _$rootScope_) {
            // The injector unwraps the underscores (_) from around the parameter names when matching
            $compile = _$compile_;
            $rootScope = _$rootScope_;
        }));
        it('Replaces the element with the appropriate content', function () {
            // Compile a piece of HTML containing the directive
            element = $compile('<athletes-by-sport></athletes-by-sport>')($rootScope);
            $rootScope.$digest();
            // Check that the compiled element contains the templated content
        });
    });
    /***
     * Test for controller
     * */
    describe('athletesBySport Controller', function () {
        var _athletesBySportController;
        beforeEach(function() {
            _athletesBySportController = element.controller('athletesBySport');
        });
        it('should be Defined', inject(function () {
            expect(_athletesBySportController).toBeDefined();
        }));
    });
    /***
     * Test for service
     * */
    describe('athletesBySport Service', function () {

    });
});
