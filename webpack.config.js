var path = require('path');
var webpack = require('webpack');
var autoprefixer = require('autoprefixer');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var ManifestRevisionPlugin = require('manifest-revision-webpack-plugin');

var rootAssetPath = './mycontactapp/static/src'
var outputPath = './mycontactapp/static/dist'

module.exports = {
    entry: [rootAssetPath + '/scripts/main.js'],
    output: {
        path: outputPath,
        filename: 'scripts/[name].js',
        publicPath: 'http://localhost:3000/'
    },
    resolve: {
        extensions: ['', '.js', '.jsx', '.scss']
    },
    //devtool: 'source-map',
    module: {
        loaders: [{
            test: /\.(jpe?g|png|gif|svg([\?]?.*))$/i,
            loaders: [
                'file?context=' + rootAssetPath + '&name=[name].[ext]',
                'image?bypassOnDebug&optimizationLevel=7&interlaced=false'
            ]
        }, {
            test: /\.woff2?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
            loader: "url?limit=10000"
        }, {
            test: /\.(ttf|eot|svg)(\?[\s\S]+)?$/,
            loader: 'file'
        }, {
            test: [/\.js$/, /\.es6$/],
            exclude: /node_modules/,
            loader: 'babel?presets[]=react,presets[]=es2015'
        }, {
            test: /bootstrap-sass\/assets\/javascripts\//,
            loader: 'imports?jQuery=jquery'
        }, {
            test: /(\.scss|\.css)$/,
            loader: ExtractTextPlugin.extract('css-loader!postcss-loader!sass-loader')
        }]
    },
    postcss: [autoprefixer({
        browsers: ['last 2 versions']
    })],
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new ExtractTextPlugin('styles/[name].css', {
            allChunks: true
        }),
        new ManifestRevisionPlugin(outputPath + '/manifest.json', {
            rootAssetPath: rootAssetPath,
                ignorePaths: ['/styles', '/scripts']
        })
    ]
};
