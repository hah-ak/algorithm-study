const {createProxyMiddleware} = require('http-proxy-middleware');
// require는 노드에 탑재된 함수

module.exports = (app) => {
    app.use(
        ('/api','/aps'),
        createProxyMiddleware({
            target: 'http://localhost:8000',
            changeOrigin: true,
        })
    )
}