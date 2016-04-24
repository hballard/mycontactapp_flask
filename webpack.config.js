const autoprefixer = require('autoprefixer');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const path = require('path');
const webpack = require('webpack');

module.exports = {

  entry: [
    'bootstrap-loader',
    './mycontactapp/static/src/scripts/main'
  ],

  output: {
    path: path.join(__dirname, '/mycontactapp/static/dist'),
    filename: 'scripts/[name].js',
    publicPath: '/',
  },

  devtool: '#cheap-module-eval-source-map',

  resolve: { extensions: [ '', '.js', '.jsx' ] },

  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin(),
    new ExtractTextPlugin('styles/[name].css', { allChunks: true }),
  ],

  module: {
    loaders: [
      { 
        test: /\.css$/, loaders: [ 'style', 'css', 'postcss' ]
      },
      { 
        test: /\.scss$/, loaders: [ 'style', 'css', 'postcss', 'sass' ]
      },
      {
        test: /\.woff2?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        loader: "url-loader?limit=10000&mimetype=application/font-woff2&name=[name].[ext]"
      },
      {
        test: [/\.js$/, /\.es6$/],
        exclude: /node_modules/,
        loader: 'babel?presets[]=react,presets[]=es2015'
      },
      {
        test: /\.(eot|ttf|svg|gif|png)$/,
        loader: "file?name=[name].[ext]"
      },
      // Bootstrap 3
      { test: /bootstrap-sass\/assets\/javascripts\//, loader: 'imports?jQuery=jquery' },
    ],
  },

  postcss: [ autoprefixer ],

};
