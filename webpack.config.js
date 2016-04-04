var path = require('path');
var webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var autoprefixer = require('autoprefixer');

module.exports = {
    entry: ['./mycontactapp/static/src/scripts/main.js'],
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
        loaders: [{
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
        new ExtractTextPlugin(path.join('styles', '[name].css'), {
            allChunks: true
        })
    ]
};
