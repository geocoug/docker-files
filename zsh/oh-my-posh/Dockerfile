FROM zshusers/zsh:latest

RUN apt-get update && apt-get install -y \
    git \
    curl \
    vim \
    exa \
    unzip \
    && rm -rf /var/lib/apt/lists/*

RUN echo "/usr/bin/zsh" >> /etc/shells

# Install oh-my-zsh
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Install oh-my-posh
RUN curl -s https://ohmyposh.dev/install.sh | bash -s

# Install zsh-syntax-highlighting
RUN git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# Install zsh-autosuggestions
RUN git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# Add custom zshrc
COPY .zshrc /root/.zshrc

# Add custom themes
COPY .poshthemes /root/.poshthemes

# Start zsh and pipe any output to /dev/null.
# This will prevent any additional configuration steps from being displayed on container startup.
RUN echo exit | script -qec zsh /dev/null >/dev/null
