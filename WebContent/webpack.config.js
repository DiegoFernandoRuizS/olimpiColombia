var localDevConfig = require('./webpack-base.config');
localDevConfig.entry = {
    'olimpicolombia.app': './app/app'
};
//localDevConfig.devtool = 'source-map';
module.exports = localDevConfig;
