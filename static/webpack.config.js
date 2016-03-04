var path = require('path');
var webpack = require('webpack');
var ExtractTextPlugin= require('extract-text-webpack-plugin');

module.exports = {
    entry: ['./src/scripts/main.js'],
    output: {
        path: path.resolve(__dirname, './dist'),
        filename: 'scripts/[name].js',
        publicPath: 'http://localhost:3000/'
    },
    resolve: {
        extensions: ['', '.js', '.jsx', '.scss']
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
               loader: 'babel?presets[]=react,presets[]=es2015'
            },
            {
                test: /(\.scss|\.css)$/,
                loader: ExtractTextPlugin.extract('css!sass')
            }
        ]
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new ExtractTextPlugin(path.join('styles','main.css'), {
            allChunks: true
        })
    ]
};
