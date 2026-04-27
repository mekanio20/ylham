import authService from '../services/authService.js'

class AuthController {
  login = async (req, res) => {
    const result = await authService.login(req.body);
    return res.status(result.status).json(result);
  };
  
  register = async (req, res) => {
    const result = await authService.register(req.body);
    return res.status(result.status).json(result);
  };
  
  resetPassword = async (req, res) => {
    const result = await authService.resetPassword(req.body);
    return res.status(result.status).json(result);
  }
  
  verifyEmail = async (req, res) => {
    const result = await authService.verifyEmail(req.body);
    return res.status(result.status).json(result);
  }
  
  refreshToken = async (req, res) => {
    const result = await authService.refreshToken(req.body);
    return res.status(result.status).json(result);
  }
  
  me = async (req, res) => {
    const result = await authService.me(req.user.id);
    return res.status(result.status).json(result);
  };
  
  updateMe = async (req, res) => {
    const result = await authService.updateMe(req.user.id, req.body);
    return res.status(result.status).json(result);
  };
  
  listPoets = async (req, res) => {
    const result = await authService.listPoets();
    return res.status(result.status).json(result);
  };
}

export default new AuthController()