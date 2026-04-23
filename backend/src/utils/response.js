class ResponseService {
    async Success (msg, detail) {
        return {
            status: 200,
            type: 'success',
            msg: msg,
            msg_key: 'ok',
            data: detail
        }
    }
    async Created (msg, detail)  {
        return {
            status: 201,
            type: 'success',
            msg: msg,
            msg_key: 'created',
            data: detail
        }
    }    
    async BadRequest (msg, detail) {
        return {
            status: 400,
            type: 'error',
            msg: msg,
            msg_key: 'bad request',
            data: detail
        }
    }
    async Unauthorized (msg, detail) {
        return {
            status: 401,
            type: 'error',
            msg: msg,
            msg_key: 'unauthorized',
            data: detail
        }
    }
    async Forbidden (msg, detail) {
        return {
            status: 403,
            type: 'error',
            msg: msg,
            msg_key: 'forbidden',
            data: detail
        }
    }
    async NotFound (msg, detail) {
        return {
            status: 404,
            type: 'error',
            msg: msg,
            msg_key: 'not found',
            data: detail
        }
    }
}
module.exports = new ResponseService()