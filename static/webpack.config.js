var path = require('path');

module.exports = {
    entry: './src/scripts/main.js',
    output: {
        path: path.resolve(__dirname, './dist/scripts'),
        filename: '[name].js',
        publicPath: 'http://localhost:3000/'
    },
    resolve: {
        extensions: ['', '.js', '.jsx', '.less']
    },
    devtool: 'source-map',
    // proxy: {
    //   '*': {
    // target: 'http://0.0.0.0:5000',
    // secure: false,
    //   },
    // },
    module: {
        loaders: [
            {
               test: [/\.js$/, /\.es6$/],
               exclude: /node_modules/,
               loader: 'babel',
               query: {
                 cacheDirectory: true,
                 presets: ['react', 'es2015']
               }
            }
        ]
    },
};
