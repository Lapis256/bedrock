from setuptools import setup

setup(name="bedrock",
      version="0.2",
      description="A simply python library to access Minecraft: Bedrock Edition worlds.",
      keywords="minecraft bedrock leveldb",
      url="https://github.com/Lapis256/bedrock",
      packages=["bedrock"],
      install_requires=["numpy"],
      package_data={
          "bedrock": ["*.so", "LICENCE-LEVELDB"]
      },
      author="Lapis256")
