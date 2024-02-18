import json

def main(context):
    response = "RAW BODY: {}\n\nJSON: {}\n\nHEADERS: {}\n\nSCHEME: {}\n\nMETHOD: {}\n\nURL: {}\n\nHOST: {}\n\nPORT: {}\n\nPATH: {}\n\nQUERY: {}\n\nJSON QUERY: {}".format(
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
        json.dumps(context.req.query)
    )
    return context.res.send(response, 200, {"Content-Type": "text/plain"})