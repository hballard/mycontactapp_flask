var path = require('path');
var webpack = require('webpack');
var ExtractTextPlugin= require('extract-text-webpack-plugin');
var autoprefixer = require('autoprefixer');

module.exports = {
    entry: ['./mycontactiapp/static/src/scripts/main.js'],
    output: {
        path: path.resolve(__dirname, './mycontactapp/static/dist'),
        filename: 'scripts/[name].js',
        publicPath: 'http://localhost:3000/'
    },
    resolve: {
        extensions: ['', '.js', '.jsx', '.scss']
    },
    devtool: 'source-map',
    module: {
        loaders: [
            {
               test: [/\.js$/, /\.es6$/],
               exclude: /node_modules/,
               loader: 'babel?presets[]=react,presets[]=es2015'
            },
            {
                test: /(\.scss|\.css)$/,
                loader: ExtractTextPlugin.extract('css-loader!postcss-loader!sass-loader')
            }
        ]
    },
    postcss: [ autoprefixer({ browsers: ['last 2 versions'] }) ],
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new ExtractTextPlugin(path.join('styles','[name].css'), {
            allChunks: true
        })
    ]
};
