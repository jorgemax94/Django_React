var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var ExtractText = require('extract-text-webpack-plugin');

module.exports = {
    entry: path.join(__dirname, 'assets/src/js/index'),
    output: {
        path: path.join(__dirname, 'assets/dist'),
        filename: '[name]-[hash].js'
    },
    plugins: [
        new BundleTracker({
            path: __dirname,
            filename: 'webpack-stats.json'
        }),
    ],
    module: {
        rules: [{
                test: /|\.jsx?$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
            }, {
                test: /\.scss$\|\.css$/,
                use: ['style-loader', 'css-loader'],
            },
            {
                test: /\.scss$/,
                use: [
                    "style-loader", // inject the CSS information on the page
                    "css-loader", // translates CSS into CommonJS info
                    "sass-loader" // compiles SASS to CSS
                ]
            }
        ],
    },
}