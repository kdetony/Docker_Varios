docker run -it --name httpbin --rm citizenstig/httpbin
docker run -it --rm --link httpbin tutum/curl curl -X GET http://httpbin:8000/headers

#arranque envoy
docker run -it --rm envoyproxy/envoy envoy
docker run -it --name proxy --link httpbin -v $(pwd)/envoy_config.json:/etc/envoy_config.json envoyproxy/envoy envoy -c /etc/envoy_config.json

#envoy stats
docker run -it --rm --link proxy tutum/curl curl -X GET http://proxy:15000/stats

#peticion 500
docker run -it --rm --link proxy tutum/curl curl -X GET http://proxy:15001/status/500
