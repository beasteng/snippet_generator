"""Read profiles.yml and extract connection details via Python API."""
from dbt.config.profile import Profile, read_profile
from pathlib import Path
import yaml

profiles_dir = Path.home() / ".dbt"
profiles_path = profiles_dir / "profiles.yml"

raw_profiles = yaml.safe_load(profiles_path.read_text())

for profile_name, profile_data in raw_profiles.items():
    if isinstance(profile_data, dict) and "outputs" in profile_data:
        target = profile_data.get("target", "dev")
        outputs = profile_data["outputs"]
        print(f"\n🔑 Profile: {profile_name} (target: {target})")
        for out_name, out_cfg in outputs.items():
            marker = "→" if out_name == target else " "
            print(f"  {marker} {out_name}: type={out_cfg.get('type')}, "
                  f"schema={out_cfg.get('schema')}, "
                  f"threads={out_cfg.get('threads')}")
