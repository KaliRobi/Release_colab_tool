module.exports = {
    devServer:{
      proxy:{
        '^/api':{
          target : 'http://127.0.0.1:8000',
          ws: true,
          changeOrigin:true
        } 
      }
    }

        // publicPath:
    //   process.env.NODE_ENV === "production"
    //     ? "/static/dist/"
    //     : "http://127.0.0.1:8080",
    // outputDir: "../static/dist",
    // indexPath: "colab_tool/templates/index.html",
    // pages: {
    //   index: {
    //     entry: "src/main.js",
    //     title: "defects",
    //   },
    // },
    // colab_tool\templates\registration
    // defectsFront\vue.config.js

    // devServer: {
    //   devMiddleware: {
    //     publicPath: "http://127.0.0.1:8080",
    //     writeToDisk: (filePath) => filePath.endsWith("index.html"),
    //   },
    //   hot: "only",
    //   headers: { "Access-Control-Allow-Origin": "*" },
    // },
  };