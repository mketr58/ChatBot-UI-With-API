{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-24.05"; # or "unstable"

  # Use https://search.nixos.org/packages to find packages
  packages = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.virtualenv
    pkgs.python311Packages.black  # Optional: Add a popular Python code formatter
    pkgs.python311Packages.isort  # Optional: Add a Python code sorter
    pkgs.python311Packages.flake8 # Optional: Add a Python linter
  ];

  # Sets environment variables in the workspace
  env = {
    PYTHONPATH = "$HOME/.local/lib/python3.11/site-packages";
  };

  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [
      # "vscodevim.vim"  # Uncomment if you want the Vim extension for VSCode
    ];

    # Enable previews
    previews = {
      enable = true;
      previews = {
        # Example for running a Python script in a web preview:
        # web = {
        #   command = ["python" "app.py"];
        #   manager = "web";
        #   env = {
        #     # Set environment variables like PORT if needed
        #     PORT = "$PORT";
        #   };
        # };
      };
    };

    # Workspace lifecycle hooks
    workspace = {
      # Runs when a workspace is first created
      onCreate = {
        # Example: Set up a virtual environment and install dependencies
        install_dependencies = ''
          python3 -m venv .venv
          . .venv/bin/activate
          pip install -r requirements.txt  # Assuming a requirements.txt file exists
        '';
      };
      # Runs when the workspace is (re)started
      onStart = {
        # Example: Run a background task like starting a Python server
        # start-server = "python3 -m http.server";
      };
    };
  };
}
