import img from "../assets/img.png"

const Header = () => (
  <div className="bg-gradient-to-br from-gray-800 to-gray-600 px-6 py-4 shadow-md">
    <div className="flex items-center space-x-4">
      {/* Image container */}
      <div className="p-1 rounded-full bg-white shadow-lg">
        <img
          src={img}              // bot image
          alt="Bot"
          className="w-12 h-12 rounded-full object-cover"
        />
      </div>

      {/* Text section */}
      <div>
        <h1 className="text-xl font-semibold text-cyan-400">Medical Assistant</h1>
        <p className="text-sm text-gray-200">AI-powered medical information assistant</p>
      </div>
    </div>
  </div>
);

export default Header;
