%% File: hello.erl
-module(hello).
-export([main/1]).

main(_) ->
    io:fwrite("Hello, World!~n").
