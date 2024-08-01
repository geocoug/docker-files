FROM zshusers/zsh:latest

RUN apt-get update && apt-get install -y \
    git \
    curl \
    vim \
    exa \
    && rm -rf /var/lib/apt/lists/*

RUN echo "/usr/bin/zsh" >> /etc/shells

# Install oh-my-zsh
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Install powerlevel10k
RUN git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k \
    && echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc

# Install zsh-syntax-highlighting
RUN git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# Install zsh-autosuggestions
RUN git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# Configure powerlevel10k
RUN curl https://raw.githubusercontent.com/geocoug/dotfiles/main/.p10k.zsh -o /root/.p10k.zsh

# Add custom zshrc
COPY .zshrc /root/.zshrc

# Start zsh and pipe any output to /dev/null.
# This will prevent any additional configuration steps from being displayed on container startup.
RUN echo exit | script -qec zsh /dev/null >/dev/null
