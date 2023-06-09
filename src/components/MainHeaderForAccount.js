import { Link } from "react-router-dom";
import settings from "../static/images/settings.png";

export default function MainHeaderForAccount() {
  return (
    <div className = "top-bar">
      <Link to="/account" id = "back-button"><span>〈</span></Link>
      <div id="top-title">Allergenius</div>
    </div>
  )
}