import json
import os

def main(context):
    variables = os.environ
    envs = []
    for key, value in variables.items():
        envs.append(f"{key}: {value}")
    response = "RAW BODY: {}\n\nJSON: {}\n\nHEADERS: {}\n\nSCHEME: {}\n\nMETHOD: {}\n\nURL: {}\n\nHOST: {}\n\nPORT: {}\n\nPATH: {}\n\nQUERY: {}\n\nJSON QUERY: {}\n\n{}".format(
        context.req.body_raw,
        context.req.body,
        context.req.headers,
        context.req.scheme,
        context.req.method,
        context.req.url,
        context.req.host,
        context.req.port,
        context.req.path,
        context.req.query_string,
        context.req.query,
        "\n\n".join(envs)
    )
    return context.res.send(response, 200, {"Content-Type": "text/plain"})